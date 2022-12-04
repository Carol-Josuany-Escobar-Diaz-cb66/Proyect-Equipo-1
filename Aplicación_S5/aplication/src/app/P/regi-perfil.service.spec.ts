import { TestBed } from '@angular/core/testing';

import { RegiPerfilService } from './regi-perfil.service';

describe('RegiPerfilService', () => {
  let service: RegiPerfilService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RegiPerfilService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
