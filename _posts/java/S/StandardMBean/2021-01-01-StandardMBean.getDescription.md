---
title: StandardMBean.getDescription()
permalink: Java/StandardMBean/getDescription
date: 2021-01-11
key: JavaJava.S.StandardMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardMBean.metodos valor="getDescription" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected String getDescription(MBeanAttributeInfo info)
protected String getDescription(MBeanConstructorInfo info)
protected String getDescription(MBeanConstructorInfo ctor, MBeanParameterInfo param, int sequence)
protected String getDescription(MBeanFeatureInfo info)
protected String getDescription(MBeanInfo info)
protected String getDescription(MBeanOperationInfo info)
protected String getDescription(MBeanOperationInfo op, MBeanParameterInfo param, int sequence)
~~~

## Parámetros
* **MBeanAttributeInfo info**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanAttributeInfo info" %}
* **MBeanOperationInfo op**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanOperationInfo op" %}
* **int sequence**,  {% include w3api/param_description.html metodo=_dato parametro="int sequence" %}
* **MBeanFeatureInfo info**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanFeatureInfo info" %}
* **MBeanInfo info**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanInfo info" %}
* **MBeanParameterInfo param**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanParameterInfo param" %}
* **MBeanConstructorInfo info**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanConstructorInfo info" %}
* **MBeanOperationInfo info**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanOperationInfo info" %}
* **MBeanConstructorInfo ctor**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanConstructorInfo ctor" %}

## Clase Padre
[StandardMBean](/Java/StandardMBean/)

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
