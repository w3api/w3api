---
title: MonitorMBean.addObservedObject()
permalink: Java/MonitorMBean/addObservedObject
date: 2021-01-11
key: JavaJava.M.MonitorMBean
category: java
tags: ['java se', 'javax.management.monitor', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MonitorMBean.metodos valor="addObservedObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addObservedObject(ObjectName object) throws IllegalArgumentException
~~~

## Parámetros
* **ObjectName object**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName object" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
