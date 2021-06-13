---
title: X509EncodedKeySpec.X509EncodedKeySpec()
permalink: /Java/X509EncodedKeySpec/X509EncodedKeySpec/
date: 2021-01-11
key: Java.X.X509EncodedKeySpec
category: Java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509EncodedKeySpec.constructores valor="X509EncodedKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public X509EncodedKeySpec(byte[] encodedKey)
public X509EncodedKeySpec(byte[] encodedKey, String algorithm)
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **byte[] encodedKey**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] encodedKey" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[X509EncodedKeySpec](/Java/X509EncodedKeySpec/)

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
