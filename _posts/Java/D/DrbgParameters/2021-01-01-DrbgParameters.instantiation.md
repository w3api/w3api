---
title: DrbgParameters.instantiation()
permalink: /Java/DrbgParameters/instantiation/
date: 2021-01-11
key: Java.D.DrbgParameters
category: Java
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
* **int strength**,  {% include w3api/param_description.html metodo=_dato parametro="int strength" %}
* **byte[] personalizationString**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] personalizationString" %}
* **DrbgParameters.Capability capability**,  {% include w3api/param_description.html metodo=_dato parametro="DrbgParameters.Capability capability" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
