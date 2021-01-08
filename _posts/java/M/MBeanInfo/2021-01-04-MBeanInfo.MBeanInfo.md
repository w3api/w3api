---
title: MBeanInfo.MBeanInfo()
permalink: Java/MBeanInfo/MBeanInfo
date: 2021-01-04
key: JavaJava.M.MBeanInfo
category: java
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
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **MBeanAttributeInfo[] attributes**,  {% include w3api/param_description.html metodo=_data parametro="MBeanAttributeInfo[] attributes" %}
* **MBeanOperationInfo[] operations**,  {% include w3api/param_description.html metodo=_data parametro="MBeanOperationInfo[] operations" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **MBeanNotificationInfo[] notifications**,  {% include w3api/param_description.html metodo=_data parametro="MBeanNotificationInfo[] notifications" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **MBeanConstructorInfo[] constructors**,  {% include w3api/param_description.html metodo=_data parametro="MBeanConstructorInfo[] constructors" %}

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
{%- for _ldc in site.data.Java.M.MBeanInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
