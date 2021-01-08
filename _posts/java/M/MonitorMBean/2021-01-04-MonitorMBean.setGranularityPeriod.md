---
title: MonitorMBean.setGranularityPeriod()
permalink: Java/MonitorMBean/setGranularityPeriod
date: 2021-01-04
key: JavaJava.M.MonitorMBean
category: java
tags: ['java se', 'javax.management.monitor', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MonitorMBean.metodos valor="setGranularityPeriod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setGranularityPeriod(long period) throws IllegalArgumentException
~~~

## Parámetros
* **long period**,  {% include w3api/param_description.html metodo=_data parametro="long period" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MonitorMBean](/Java/MonitorMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
