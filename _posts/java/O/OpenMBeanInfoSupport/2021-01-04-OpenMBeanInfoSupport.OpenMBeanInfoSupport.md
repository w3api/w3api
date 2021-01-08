---
title: OpenMBeanInfoSupport.OpenMBeanInfoSupport()
permalink: Java/OpenMBeanInfoSupport/OpenMBeanInfoSupport
date: 2021-01-04
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
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **OpenMBeanConstructorInfo[] openConstructors**,  {% include w3api/param_description.html metodo=_data parametro="OpenMBeanConstructorInfo[] openConstructors" %}
* **OpenMBeanOperationInfo[] openOperations**,  {% include w3api/param_description.html metodo=_data parametro="OpenMBeanOperationInfo[] openOperations" %}
* **MBeanNotificationInfo[] notifications**,  {% include w3api/param_description.html metodo=_data parametro="MBeanNotificationInfo[] notifications" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **OpenMBeanAttributeInfo[] openAttributes**,  {% include w3api/param_description.html metodo=_data parametro="OpenMBeanAttributeInfo[] openAttributes" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}

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
{%- for _ldc in site.data.Java.O.OpenMBeanInfoSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
