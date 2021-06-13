---
title: GaugeMonitor.setThresholds()
permalink: /Java/GaugeMonitor/setThresholds/
date: 2021-01-11
key: Java.G.GaugeMonitor
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GaugeMonitor.metodos valor="setThresholds" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setThresholds(Number highValue, Number lowValue) throws IllegalArgumentException
~~~

## Parámetros
* **Number lowValue**,  {% include w3api/param_description.html metodo=_dato parametro="Number lowValue" %}
* **Number highValue**,  {% include w3api/param_description.html metodo=_dato parametro="Number highValue" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GaugeMonitor](/Java/GaugeMonitor/)

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
