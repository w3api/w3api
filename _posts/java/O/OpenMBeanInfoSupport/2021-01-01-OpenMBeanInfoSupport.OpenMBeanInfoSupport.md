---
title: OpenMBeanInfoSupport.OpenMBeanInfoSupport()
permalink: /Java/OpenMBeanInfoSupport/OpenMBeanInfoSupport/
date: 2021-01-11
key: JavaJava.O.OpenMBeanInfoSupport
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OpenMBeanInfoSupport.constructores valor="OpenMBeanInfoSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OpenMBeanInfoSupport(String className, String description, OpenMBeanAttributeInfo[] openAttributes, OpenMBeanConstructorInfo[] openConstructors, OpenMBeanOperationInfo[] openOperations, MBeanNotificationInfo[] notifications)
public OpenMBeanInfoSupport(String className, String description, OpenMBeanAttributeInfo[] openAttributes, OpenMBeanConstructorInfo[] openConstructors, OpenMBeanOperationInfo[] openOperations, MBeanNotificationInfo[] notifications, Descriptor descriptor)
~~~

## Parámetros
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **OpenMBeanConstructorInfo[] openConstructors**,  {% include w3api/param_description.html metodo=_dato parametro="OpenMBeanConstructorInfo[] openConstructors" %}
* **OpenMBeanAttributeInfo[] openAttributes**,  {% include w3api/param_description.html metodo=_dato parametro="OpenMBeanAttributeInfo[] openAttributes" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **OpenMBeanOperationInfo[] openOperations**,  {% include w3api/param_description.html metodo=_dato parametro="OpenMBeanOperationInfo[] openOperations" %}
* **MBeanNotificationInfo[] notifications**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanNotificationInfo[] notifications" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[ArrayStoreException](/Java/ArrayStoreException/)

## Clase Padre
[OpenMBeanInfoSupport](/Java/OpenMBeanInfoSupport/)

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
