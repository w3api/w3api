---
title: DrbgParameters.nextBytes()
permalink: /Java/DrbgParameters/nextBytes/
date: 2021-01-11
key: Java.D.DrbgParameters
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DrbgParameters.metodos valor="nextBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DrbgParameters.NextBytes nextBytes(int strength, boolean predictionResistance, byte[] additionalInput)
~~~

## Parámetros
* **int strength**,  {% include w3api/param_description.html metodo=_dato parametro="int strength" %}
* **boolean predictionResistance**,  {% include w3api/param_description.html metodo=_dato parametro="boolean predictionResistance" %}
* **byte[] additionalInput**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] additionalInput" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DrbgParameters](/Java/DrbgParameters/)

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
