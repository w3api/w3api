---
title: ModelMBeanInfoSupport.ModelMBeanInfoSupport()
permalink: Java/ModelMBeanInfoSupport/ModelMBeanInfoSupport
date: 2021-01-04
key: JavaJava.M.ModelMBeanInfoSupport
category: java
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
* **ModelMBeanAttributeInfo[] attributes**,  {% include w3api/param_description.html metodo=_data parametro="ModelMBeanAttributeInfo[] attributes" %}
* **Descriptor mbeandescriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor mbeandescriptor" %}
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **ModelMBeanNotificationInfo[] notifications**,  {% include w3api/param_description.html metodo=_data parametro="ModelMBeanNotificationInfo[] notifications" %}
* **ModelMBeanInfo mbi**,  {% include w3api/param_description.html metodo=_data parametro="ModelMBeanInfo mbi" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **ModelMBeanConstructorInfo[] constructors**,  {% include w3api/param_description.html metodo=_data parametro="ModelMBeanConstructorInfo[] constructors" %}
* **ModelMBeanOperationInfo[] operations**,  {% include w3api/param_description.html metodo=_data parametro="ModelMBeanOperationInfo[] operations" %}

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
{%- for _ldc in site.data.Java.M.ModelMBeanInfoSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
