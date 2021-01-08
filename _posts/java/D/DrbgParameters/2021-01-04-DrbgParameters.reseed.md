---
title: DrbgParameters.reseed()
permalink: Java/DrbgParameters/reseed
date: 2021-01-04
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
* **boolean predictionResistance**,  {% include w3api/param_description.html metodo=_data parametro="boolean predictionResistance" %}
* **byte[] additionalInput**,  {% include w3api/param_description.html metodo=_data parametro="byte[] additionalInput" %}

## Clase Padre
[DrbgParameters](/Java/DrbgParameters/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DrbgParameters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
