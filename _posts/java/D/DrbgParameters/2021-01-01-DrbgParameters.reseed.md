---
title: DrbgParameters.reseed()
permalink: Java/DrbgParameters/reseed
date: 2021-01-11
key: JavaJava.D.DrbgParameters
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DrbgParameters.metodos valor="reseed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DrbgParameters.Reseed reseed(boolean predictionResistance, byte[] additionalInput)
~~~

## Parámetros
* **byte[] additionalInput**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] additionalInput" %}
* **boolean predictionResistance**,  {% include w3api/param_description.html metodo=_dato parametro="boolean predictionResistance" %}

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
