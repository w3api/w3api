---
title: GaugeMonitorMBean.getDerivedGauge()
permalink: Java/GaugeMonitorMBean/getDerivedGauge
date: 2021-01-11
key: JavaJava.G.GaugeMonitorMBean
category: java
tags: ['java se', 'javax.management.monitor', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GaugeMonitorMBean.metodos valor="getDerivedGauge" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated Number getDerivedGauge()
Number getDerivedGauge(ObjectName object)
~~~

## Parámetros
* **ObjectName object**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName object" %}

## Clase Padre
[GaugeMonitorMBean](/Java/GaugeMonitorMBean/)

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
