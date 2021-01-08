---
title: StandardMBean.getParameterName()
permalink: Java/StandardMBean/getParameterName
date: 2021-01-04
key: JavaJava.S.StandardMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardMBean.metodos valor="getParameterName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected String getParameterName(MBeanConstructorInfo ctor, MBeanParameterInfo param, int sequence)
protected String getParameterName(MBeanOperationInfo op, MBeanParameterInfo param, int sequence)
~~~

## Parámetros
* **int sequence**,  {% include w3api/param_description.html metodo=_data parametro="int sequence" %}
* **MBeanConstructorInfo ctor**,  {% include w3api/param_description.html metodo=_data parametro="MBeanConstructorInfo ctor" %}
* **MBeanOperationInfo op**,  {% include w3api/param_description.html metodo=_data parametro="MBeanOperationInfo op" %}
* **MBeanParameterInfo param**,  {% include w3api/param_description.html metodo=_data parametro="MBeanParameterInfo param" %}

## Clase Padre
[StandardMBean](/Java/StandardMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
