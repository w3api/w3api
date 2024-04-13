---
title: EncodedKeySpec.EncodedKeySpec()
permalink: /Java/EncodedKeySpec/EncodedKeySpec/
date: 2021-01-11
key: Java.E.EncodedKeySpec
category: Java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EncodedKeySpec.constructores valor="EncodedKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EncodedKeySpec(byte[] encodedKey)
protected EncodedKeySpec(byte[] encodedKey, String algorithm)
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **byte[] encodedKey**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] encodedKey" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[EncodedKeySpec](/Java/EncodedKeySpec/)

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
