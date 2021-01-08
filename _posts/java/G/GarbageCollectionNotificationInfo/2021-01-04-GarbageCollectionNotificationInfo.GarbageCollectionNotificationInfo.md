---
title: GarbageCollectionNotificationInfo.GarbageCollectionNotificationInfo()
permalink: Java/GarbageCollectionNotificationInfo/GarbageCollectionNotificationInfo
date: 2021-01-04
key: JavaJava.G.GarbageCollectionNotificationInfo
category: java
tags: ['java se', 'com.sun.management', 'jdk.management', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GarbageCollectionNotificationInfo.constructores valor="GarbageCollectionNotificationInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GarbageCollectionNotificationInfo(String gcName, String gcAction, String gcCause, GcInfo gcInfo)
~~~

## Parámetros
* **GcInfo gcInfo**,  {% include w3api/param_description.html metodo=_data parametro="GcInfo gcInfo" %}
* **String gcName**,  {% include w3api/param_description.html metodo=_data parametro="String gcName" %}
* **String gcAction**,  {% include w3api/param_description.html metodo=_data parametro="String gcAction" %}
* **String gcCause**,  {% include w3api/param_description.html metodo=_data parametro="String gcCause" %}

## Clase Padre
[GarbageCollectionNotificationInfo](/Java/GarbageCollectionNotificationInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GarbageCollectionNotificationInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
