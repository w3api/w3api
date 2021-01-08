---
title: CertPathBuilder.build()
permalink: Java/CertPathBuilder/build
date: 2021-01-04
key: JavaJava.C.CertPathBuilder
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathBuilder.metodos valor="build" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CertPathBuilderResult build(CertPathParameters params) throws CertPathBuilderException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **CertPathParameters params**,  {% include w3api/param_description.html metodo=_data parametro="CertPathParameters params" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [CertPathBuilderException](/Java/CertPathBuilderException/)

## Clase Padre
[CertPathBuilder](/Java/CertPathBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertPathBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
