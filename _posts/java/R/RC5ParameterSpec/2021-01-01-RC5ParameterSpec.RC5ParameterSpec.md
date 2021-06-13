---
title: RC5ParameterSpec.RC5ParameterSpec()
permalink: Java/RC5ParameterSpec/RC5ParameterSpec
date: 2021-01-11
key: Java.R.RC5ParameterSpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RC5ParameterSpec.constructores valor="RC5ParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RC5ParameterSpec(int version, int rounds, int wordSize)
public RC5ParameterSpec(int version, int rounds, int wordSize, byte[] iv)
public RC5ParameterSpec(int version, int rounds, int wordSize, byte[] iv, int offset)
~~~

## Parámetros
* **int version**,  {% include w3api/param_description.html metodo=_dato parametro="int version" %}
* **byte[] iv**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] iv" %}
* **int wordSize**,  {% include w3api/param_description.html metodo=_dato parametro="int wordSize" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int rounds**,  {% include w3api/param_description.html metodo=_dato parametro="int rounds" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RC5ParameterSpec](/Java/RC5ParameterSpec/)

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
