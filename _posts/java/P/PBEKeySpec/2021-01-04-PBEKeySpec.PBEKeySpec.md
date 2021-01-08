---
title: PBEKeySpec.PBEKeySpec()
permalink: Java/PBEKeySpec/PBEKeySpec
date: 2021-01-04
key: JavaJava.P.PBEKeySpec
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
* **byte[] salt**,  {% include w3api/param_description.html metodo=_data parametro="byte[] salt" %}
* **int iterationCount**,  {% include w3api/param_description.html metodo=_data parametro="int iterationCount" %}
* **char[] password**,  {% include w3api/param_description.html metodo=_data parametro="char[] password" %}
* **int keyLength**,  {% include w3api/param_description.html metodo=_data parametro="int keyLength" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PBEKeySpec](/Java/PBEKeySpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PBEKeySpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
