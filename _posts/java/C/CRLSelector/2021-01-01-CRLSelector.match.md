---
title: CRLSelector.match()
permalink: /Java/CRLSelector/match/
date: 2021-01-11
key: Java.C.CRLSelector
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CRLSelector.metodos valor="match" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean match(CRL crl)
~~~

## Parámetros
* **CRL crl**,  {% include w3api/param_description.html metodo=_dato parametro="CRL crl" %}

## Clase Padre
[CRLSelector](/Java/CRLSelector/)

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
