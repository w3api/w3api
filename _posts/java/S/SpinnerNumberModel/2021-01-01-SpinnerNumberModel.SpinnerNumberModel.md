---
title: SpinnerNumberModel.SpinnerNumberModel()
permalink: Java/SpinnerNumberModel/SpinnerNumberModel
date: 2021-01-11
key: JavaJava.S.SpinnerNumberModel
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SpinnerNumberModel.constructores valor="SpinnerNumberModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SpinnerNumberModel()
public SpinnerNumberModel(double value, double minimum, double maximum, double stepSize)
public SpinnerNumberModel(int value, int minimum, int maximum, int stepSize)
public SpinnerNumberModel(Number value, Comparable<?> minimum, Comparable<?> maximum, Number stepSize)
~~~

## Parámetros
* **double stepSize**,  {% include w3api/param_description.html metodo=_dato parametro="double stepSize" %}
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **int minimum**,  {% include w3api/param_description.html metodo=_dato parametro="int minimum" %}
* **int maximum**,  {% include w3api/param_description.html metodo=_dato parametro="int maximum" %}
* **double value**,  {% include w3api/param_description.html metodo=_dato parametro="double value" %}
* **double minimum**,  {% include w3api/param_description.html metodo=_dato parametro="double minimum" %}
* **Comparable&lt;?&gt; maximum**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<?> maximum" %}
* **Number stepSize**,  {% include w3api/param_description.html metodo=_dato parametro="Number stepSize" %}
* **Comparable&lt;?&gt; minimum**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<?> minimum" %}
* **double maximum**,  {% include w3api/param_description.html metodo=_dato parametro="double maximum" %}
* **int stepSize**,  {% include w3api/param_description.html metodo=_dato parametro="int stepSize" %}
* **Number value**,  {% include w3api/param_description.html metodo=_dato parametro="Number value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SpinnerNumberModel](/Java/SpinnerNumberModel/)

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
