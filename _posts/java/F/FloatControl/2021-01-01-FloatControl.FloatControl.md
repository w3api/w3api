---
title: FloatControl.FloatControl()
permalink: /Java/FloatControl/FloatControl/
date: 2021-01-11
key: Java.F.FloatControl
category: Java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FloatControl.constructores valor="FloatControl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected FloatControl(FloatControl.Type type, float minimum, float maximum, float precision, int updatePeriod, float initialValue, String units)
protected FloatControl(FloatControl.Type type, float minimum, float maximum, float precision, int updatePeriod, float initialValue, String units, String minLabel, String midLabel, String maxLabel)
~~~

## Parámetros
* **float initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="float initialValue" %}
* **float maximum**,  {% include w3api/param_description.html metodo=_dato parametro="float maximum" %}
* **String units**,  {% include w3api/param_description.html metodo=_dato parametro="String units" %}
* **FloatControl.Type type**,  {% include w3api/param_description.html metodo=_dato parametro="FloatControl.Type type" %}
* **String maxLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String maxLabel" %}
* **float precision**,  {% include w3api/param_description.html metodo=_dato parametro="float precision" %}
* **int updatePeriod**,  {% include w3api/param_description.html metodo=_dato parametro="int updatePeriod" %}
* **float minimum**,  {% include w3api/param_description.html metodo=_dato parametro="float minimum" %}
* **String midLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String midLabel" %}
* **String minLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String minLabel" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FloatControl](/Java/FloatControl/)

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
