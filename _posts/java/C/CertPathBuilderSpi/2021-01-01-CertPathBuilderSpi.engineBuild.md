---
title: CertPathBuilderSpi.engineBuild()
permalink: /Java/CertPathBuilderSpi/engineBuild/
date: 2021-01-11
key: Java.C.CertPathBuilderSpi
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathBuilderSpi.metodos valor="engineBuild" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CertPathBuilderResult engineBuild(CertPathParameters params) throws CertPathBuilderException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **CertPathParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="CertPathParameters params" %}

## Excepciones
[CertPathBuilderException](/Java/CertPathBuilderException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[CertPathBuilderSpi](/Java/CertPathBuilderSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
