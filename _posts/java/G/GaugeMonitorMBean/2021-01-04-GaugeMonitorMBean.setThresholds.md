---
title: GaugeMonitorMBean.setThresholds()
permalink: Java/GaugeMonitorMBean/setThresholds
date: 2021-01-04
key: JavaJava.G.GaugeMonitorMBean
category: java
tags: ['java se', 'javax.management.monitor', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GaugeMonitorMBean.metodos valor="setThresholds" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setThresholds(Number highValue, Number lowValue) throws IllegalArgumentException
~~~

## Parámetros
* **Number highValue**,  {% include w3api/param_description.html metodo=_data parametro="Number highValue" %}
* **Number lowValue**,  {% include w3api/param_description.html metodo=_data parametro="Number lowValue" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GaugeMonitorMBean](/Java/GaugeMonitorMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GaugeMonitorMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
