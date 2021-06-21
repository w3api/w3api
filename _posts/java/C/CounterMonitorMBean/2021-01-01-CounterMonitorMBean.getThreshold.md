---
title: CounterMonitorMBean.getThreshold()
permalink: /Java/CounterMonitorMBean/getThreshold/
date: 2021-01-11
key: Java.C.CounterMonitorMBean
category: Java
tags: ['java se', 'javax.management.monitor', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CounterMonitorMBean.metodos valor="getThreshold" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated Number getThreshold()
Number getThreshold(ObjectName object)
~~~

## Parámetros
* **ObjectName object**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName object" %}

## Clase Padre
[CounterMonitorMBean](/Java/CounterMonitorMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
