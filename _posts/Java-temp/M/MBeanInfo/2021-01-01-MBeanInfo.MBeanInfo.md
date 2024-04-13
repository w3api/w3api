---
title: MBeanInfo.MBeanInfo()
permalink: /Java/MBeanInfo/MBeanInfo/
date: 2021-01-11
key: Java.M.MBeanInfo
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanInfo.constructores valor="MBeanInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanInfo(String className, String description, MBeanAttributeInfo[] attributes, MBeanConstructorInfo[] constructors, MBeanOperationInfo[] operations, MBeanNotificationInfo[] notifications) throws IllegalArgumentException
public MBeanInfo(String className, String description, MBeanAttributeInfo[] attributes, MBeanConstructorInfo[] constructors, MBeanOperationInfo[] operations, MBeanNotificationInfo[] notifications, Descriptor descriptor) throws IllegalArgumentException
~~~

## Parámetros
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **MBeanAttributeInfo[] attributes**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanAttributeInfo[] attributes" %}
* **MBeanConstructorInfo[] constructors**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanConstructorInfo[] constructors" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **MBeanNotificationInfo[] notifications**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanNotificationInfo[] notifications" %}
* **MBeanOperationInfo[] operations**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanOperationInfo[] operations" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MBeanInfo](/Java/MBeanInfo/)

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
