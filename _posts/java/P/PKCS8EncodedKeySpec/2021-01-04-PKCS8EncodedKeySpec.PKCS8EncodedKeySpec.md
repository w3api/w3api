---
title: PKCS8EncodedKeySpec.PKCS8EncodedKeySpec()
permalink: Java/PKCS8EncodedKeySpec/PKCS8EncodedKeySpec
date: 2021-01-04
key: JavaJava.P.PKCS8EncodedKeySpec
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKCS8EncodedKeySpec.constructores valor="PKCS8EncodedKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PKCS8EncodedKeySpec(byte[] encodedKey)
public PKCS8EncodedKeySpec(byte[] encodedKey, String algorithm)
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **byte[] encodedKey**,  {% include w3api/param_description.html metodo=_data parametro="byte[] encodedKey" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PKCS8EncodedKeySpec](/Java/PKCS8EncodedKeySpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PKCS8EncodedKeySpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
