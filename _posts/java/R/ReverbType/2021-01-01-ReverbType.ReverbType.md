---
title: ReverbType.ReverbType()
permalink: Java/ReverbType/ReverbType
date: 2021-01-11
key: Java.R.ReverbType
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReverbType.constructores valor="ReverbType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ReverbType(String name, int earlyReflectionDelay, float earlyReflectionIntensity, int lateReflectionDelay, float lateReflectionIntensity, int decayTime)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **int decayTime**,  {% include w3api/param_description.html metodo=_dato parametro="int decayTime" %}
* **float lateReflectionIntensity**,  {% include w3api/param_description.html metodo=_dato parametro="float lateReflectionIntensity" %}
* **int lateReflectionDelay**,  {% include w3api/param_description.html metodo=_dato parametro="int lateReflectionDelay" %}
* **float earlyReflectionIntensity**,  {% include w3api/param_description.html metodo=_dato parametro="float earlyReflectionIntensity" %}
* **int earlyReflectionDelay**,  {% include w3api/param_description.html metodo=_dato parametro="int earlyReflectionDelay" %}

## Clase Padre
[ReverbType](/Java/ReverbType/)

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
