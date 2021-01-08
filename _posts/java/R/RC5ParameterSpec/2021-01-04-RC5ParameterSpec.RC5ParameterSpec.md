---
title: RC5ParameterSpec.RC5ParameterSpec()
permalink: Java/RC5ParameterSpec/RC5ParameterSpec
date: 2021-01-04
key: JavaJava.R.RC5ParameterSpec
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
* **int rounds**,  {% include w3api/param_description.html metodo=_data parametro="int rounds" %}
* **int wordSize**,  {% include w3api/param_description.html metodo=_data parametro="int wordSize" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **byte[] iv**,  {% include w3api/param_description.html metodo=_data parametro="byte[] iv" %}
* **int version**,  {% include w3api/param_description.html metodo=_data parametro="int version" %}

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
{%- for _ldc in site.data.Java.R.RC5ParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
