---
title: MBeanNotificationInfo.MBeanNotificationInfo()
permalink: Java/MBeanNotificationInfo/MBeanNotificationInfo
date: 2021-01-04
key: JavaJava.M.MBeanNotificationInfo
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanNotificationInfo.constructores valor="MBeanNotificationInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanNotificationInfo(String[] notifTypes, String name, String description)
public MBeanNotificationInfo(String[] notifTypes, String name, String description, Descriptor descriptor)
~~~

## Parámetros
* **String[] notifTypes**,  {% include w3api/param_description.html metodo=_data parametro="String[] notifTypes" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}

## Clase Padre
[MBeanNotificationInfo](/Java/MBeanNotificationInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanNotificationInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
