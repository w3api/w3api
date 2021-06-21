---
title: Certificate.CertificateRep.readResolve()
permalink: /Java/Certificate/CertificateRep/readResolve/
date: 2021-01-11
key: Java.C.Certificate.CertificateRep
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Certificate.CertificateRep.metodos valor="readResolve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Object readResolve() throws ObjectStreamException
~~~

## Excepciones
[ObjectStreamException](/Java/ObjectStreamException/)

## Clase Padre
[Certificate.CertificateRep](/Java/Certificate/CertificateRep/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
