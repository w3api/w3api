---
title: ModelMBeanInfoSupport.ModelMBeanInfoSupport()
permalink: /Java/ModelMBeanInfoSupport/ModelMBeanInfoSupport/
date: 2021-01-11
key: Java.M.ModelMBeanInfoSupport
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanInfoSupport.constructores valor="ModelMBeanInfoSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModelMBeanInfoSupport(String className, String description, ModelMBeanAttributeInfo[] attributes, ModelMBeanConstructorInfo[] constructors, ModelMBeanOperationInfo[] operations, ModelMBeanNotificationInfo[] notifications)
public ModelMBeanInfoSupport(String className, String description, ModelMBeanAttributeInfo[] attributes, ModelMBeanConstructorInfo[] constructors, ModelMBeanOperationInfo[] operations, ModelMBeanNotificationInfo[] notifications, Descriptor mbeandescriptor)
public ModelMBeanInfoSupport(ModelMBeanInfo mbi)
~~~

## Parámetros
* **ModelMBeanAttributeInfo[] attributes**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanAttributeInfo[] attributes" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **ModelMBeanNotificationInfo[] notifications**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanNotificationInfo[] notifications" %}
* **ModelMBeanConstructorInfo[] constructors**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanConstructorInfo[] constructors" %}
* **ModelMBeanInfo mbi**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanInfo mbi" %}
* **Descriptor mbeandescriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor mbeandescriptor" %}
* **ModelMBeanOperationInfo[] operations**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanOperationInfo[] operations" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanInfoSupport](/Java/ModelMBeanInfoSupport/)

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
