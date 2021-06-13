---
title: PBEKeySpec.PBEKeySpec()
permalink: /Java/PBEKeySpec/PBEKeySpec/
date: 2021-01-11
key: Java.P.PBEKeySpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PBEKeySpec.constructores valor="PBEKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PBEKeySpec(char[] password)
public PBEKeySpec(char[] password, byte[] salt, int iterationCount)
public PBEKeySpec(char[] password, byte[] salt, int iterationCount, int keyLength)
~~~

## Parámetros
* **char[] password**,  {% include w3api/param_description.html metodo=_dato parametro="char[] password" %}
* **int keyLength**,  {% include w3api/param_description.html metodo=_dato parametro="int keyLength" %}
* **byte[] salt**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] salt" %}
* **int iterationCount**,  {% include w3api/param_description.html metodo=_dato parametro="int iterationCount" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PBEKeySpec](/Java/PBEKeySpec/)

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
