---
title: AdjustmentEvent.AdjustmentEvent()
permalink: Java/AdjustmentEvent/AdjustmentEvent
date: 2021-01-04
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
* **boolean isAdjusting**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAdjusting" %}
* **int type**,  {% include w3api/param_description.html metodo=_data parametro="int type" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **Adjustable source**,  {% include w3api/param_description.html metodo=_data parametro="Adjustable source" %}
* **int value**,  {% include w3api/param_description.html metodo=_data parametro="int value" %}

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
{%- for _ldc in site.data.Java.A.AdjustmentEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
