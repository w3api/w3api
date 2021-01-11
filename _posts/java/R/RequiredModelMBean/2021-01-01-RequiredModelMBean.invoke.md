---
title: RequiredModelMBean.invoke()
permalink: Java/RequiredModelMBean/invoke
date: 2021-01-11
key: JavaJava.R.RequiredModelMBean
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RequiredModelMBean.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object invoke(String opName, Object[] opArgs, String[] sig) throws MBeanException, ReflectionException
~~~

## Parámetros
* **String opName**,  {% include w3api/param_description.html metodo=_dato parametro="String opName" %}
* **Object[] opArgs**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] opArgs" %}
* **String[] sig**,  {% include w3api/param_description.html metodo=_dato parametro="String[] sig" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

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
