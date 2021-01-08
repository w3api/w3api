---
title: DrbgParameters.instantiation()
permalink: Java/DrbgParameters/instantiation
date: 2021-01-04
key: JavaJava.D.DrbgParameters
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DrbgParameters.metodos valor="instantiation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DrbgParameters.Instantiation instantiation(int strength, DrbgParameters.Capability capability, byte[] personalizationString)
~~~

## Parámetros
* **DrbgParameters.Capability capability**,  {% include w3api/param_description.html metodo=_data parametro="DrbgParameters.Capability capability" %}
* **int strength**,  {% include w3api/param_description.html metodo=_data parametro="int strength" %}
* **byte[] personalizationString**,  {% include w3api/param_description.html metodo=_data parametro="byte[] personalizationString" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
