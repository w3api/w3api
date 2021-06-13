---
title: ModelMBeanNotificationInfo.ModelMBeanNotificationInfo()
permalink: /Java/ModelMBeanNotificationInfo/ModelMBeanNotificationInfo/
date: 2021-01-11
key: Java.M.ModelMBeanNotificationInfo
category: Java
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **String[] notifTypes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] notifTypes" %}
* **ModelMBeanNotificationInfo inInfo**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanNotificationInfo inInfo" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
