**********************************************************************
*** getpythia6data. This program produces data files for production
*** fluxes generated with Pythia6. Produced from wimpyields.f in
*** the examples/aux directory in DarkSUSY6 trunk.
*** Author (wimpyields): Joakim Edsjo, edsjo@fysik.su.se
*** Modified (getpythia6data): Carl Niblaeus, carl.niblaeus@fysik.su.se
*** Date: October 26, 2017
**********************************************************************

      program getpythia6data
      implicit none

      real*8 dsanyield_sim, dsseyield_sim
      integer annpdg,yieldpdg,diff,ndec,ntot
      real*8 yield,mwimp,decmin,e
      character*1 hel
      integer i,istat
      character*80 filename
      integer yieldpdgs(4),annpdgs(4),j,k
      character*5 char_mwimp,char_ann,char_yield

      call dsinit

c...Setup, see header of src/an_yield/dsanyield_sim.f for details
      
c      annpdg=5                  ! PDG code of annihilation products
c      yieldpdg=22               ! PDG code of yield of interest
      annpdgs(1)=5              ! b
      annpdgs(2)=6              ! t
      annpdgs(3)=15             ! tau
      annpdgs(4)=24             ! W
      yieldpdgs(1)=-11          ! e+
      yieldpdgs(2)=-2212        ! pbar
      yieldpdgs(3)=14           ! nu_mu
      yieldpdgs(4)=22           ! gamma  
      mwimp=100.d0              ! WIMP mass (GeV)
      hel='0'                   ! helicity state, '0'=unpolarized
      diff=1                    ! differential yields
      decmin=-10.d0             ! lowest energy, 10^-decmin * mwimp
      ndec=25                   ! number of bins per decade
                                ! total number of bins = ndec*(-decmin)
      
      do j=1,4
         write(char_mwimp,'(I5)') int(mwimp)
         write(char_ann,'(I5)') annpdgs(j)
         do k=1,4
            write(char_yield,'(I5)') yieldpdgs(k)
            filename='da-pyt6-mx'//trim(adjustl(char_mwimp))
     &               //'-ch'//trim(adjustl(char_ann))
     &               //'-y'//trim(adjustl(char_yield))//'.dat'
            write(*,*) 'Running wimpyields for filename ',filename
cc      filename='yield.dat'      

c...Preliminary calculations
            ntot=ndec*(-decmin)
c            ntot=200

c...Open file and perform calculation      
            open(unit=47,file=filename,status='unknown',form='formatted')
            if (diff.eq.1) then
               write(47,'(A)') '#  i        E [GeV]   yield [GeV^-1 ann^-1]'
            else
               write(47,'(A)') '#  i        E [GeV]   yield [ann^-1]'
            endif
            
            do i=1,ntot
               e=mwimp*10**(decmin-(dble(i)-0.5d0)/abs(ntot)*decmin)
c               e=mwimp*(1.d0/dble(ntot)/2.d0+dble(i-1)/dble(ntot))
               yield=dsanyield_sim(mwimp,e,annpdgs(j),hel,yieldpdgs(k),diff,istat)
               write(47,100) i,e,yield
            enddo
            close(47)
         enddo
      enddo
      
100   format(I4,1x,E14.6,1x,E14.6)
      end
