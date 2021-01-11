---
title: RequiredModelMBean.preRegister()
permalink: Java/RequiredModelMBean/preRegister
date: 2021-01-11
key: JavaJava.R.RequiredModelMBean
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RequiredModelMBean.metodos valor="preRegister" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ObjectName preRegister(MBeanServer server, ObjectName name) throws Exception
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **MBeanServer server**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServer server" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[RequiredModelMBean](/Java/RequiredModelMBean/)

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
