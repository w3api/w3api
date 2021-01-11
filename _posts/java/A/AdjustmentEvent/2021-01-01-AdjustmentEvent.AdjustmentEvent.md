---
title: AdjustmentEvent.AdjustmentEvent()
permalink: Java/AdjustmentEvent/AdjustmentEvent
date: 2021-01-11
key: JavaJava.A.AdjustmentEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AdjustmentEvent.constructores valor="AdjustmentEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AdjustmentEvent(Adjustable source, int id, int type, int value)
public AdjustmentEvent(Adjustable source, int id, int type, int value, boolean isAdjusting)
~~~

## Parámetros
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}
* **boolean isAdjusting**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAdjusting" %}
* **Adjustable source**,  {% include w3api/param_description.html metodo=_dato parametro="Adjustable source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AdjustmentEvent](/Java/AdjustmentEvent/)

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
