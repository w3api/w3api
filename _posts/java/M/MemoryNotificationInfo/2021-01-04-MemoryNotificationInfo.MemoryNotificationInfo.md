---
title: MemoryNotificationInfo.MemoryNotificationInfo()
permalink: Java/MemoryNotificationInfo/MemoryNotificationInfo
date: 2021-01-04
key: JavaJava.M.MemoryNotificationInfo
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MemoryNotificationInfo.constructores valor="MemoryNotificationInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MemoryNotificationInfo(String poolName, MemoryUsage usage, long count)
~~~

## Parámetros
* **MemoryUsage usage**,  {% include w3api/param_description.html metodo=_data parametro="MemoryUsage usage" %}
* **long count**,  {% include w3api/param_description.html metodo=_data parametro="long count" %}
* **String poolName**,  {% include w3api/param_description.html metodo=_data parametro="String poolName" %}

## Clase Padre
[MemoryNotificationInfo](/Java/MemoryNotificationInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemoryNotificationInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
