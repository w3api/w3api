---
title: FloatControl.FloatControl()
permalink: Java/FloatControl/FloatControl
date: 2021-01-04
key: JavaJava.F.FloatControl
category: java
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
* **FloatControl.Type type**,  {% include w3api/param_description.html metodo=_data parametro="FloatControl.Type type" %}
* **float minimum**,  {% include w3api/param_description.html metodo=_data parametro="float minimum" %}
* **String units**,  {% include w3api/param_description.html metodo=_data parametro="String units" %}
* **String minLabel**,  {% include w3api/param_description.html metodo=_data parametro="String minLabel" %}
* **float initialValue**,  {% include w3api/param_description.html metodo=_data parametro="float initialValue" %}
* **float maximum**,  {% include w3api/param_description.html metodo=_data parametro="float maximum" %}
* **String midLabel**,  {% include w3api/param_description.html metodo=_data parametro="String midLabel" %}
* **float precision**,  {% include w3api/param_description.html metodo=_data parametro="float precision" %}
* **String maxLabel**,  {% include w3api/param_description.html metodo=_data parametro="String maxLabel" %}
* **int updatePeriod**,  {% include w3api/param_description.html metodo=_data parametro="int updatePeriod" %}

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
{%- for _ldc in site.data.Java.F.FloatControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
