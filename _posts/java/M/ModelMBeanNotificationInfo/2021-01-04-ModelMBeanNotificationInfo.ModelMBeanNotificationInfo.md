---
title: ModelMBeanNotificationInfo.ModelMBeanNotificationInfo()
permalink: Java/ModelMBeanNotificationInfo/ModelMBeanNotificationInfo
date: 2021-01-04
key: JavaJava.M.ModelMBeanNotificationInfo
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanNotificationInfo.constructores valor="ModelMBeanNotificationInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModelMBeanNotificationInfo(String[] notifTypes, String name, String description)
public ModelMBeanNotificationInfo(String[] notifTypes, String name, String description, Descriptor descriptor)
public ModelMBeanNotificationInfo(ModelMBeanNotificationInfo inInfo)
~~~

## Parámetros
* **String[] notifTypes**,  {% include w3api/param_description.html metodo=_data parametro="String[] notifTypes" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **ModelMBeanNotificationInfo inInfo**,  {% include w3api/param_description.html metodo=_data parametro="ModelMBeanNotificationInfo inInfo" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanNotificationInfo](/Java/ModelMBeanNotificationInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModelMBeanNotificationInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
