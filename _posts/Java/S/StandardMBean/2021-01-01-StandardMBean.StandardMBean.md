---
title: StandardMBean.StandardMBean()
permalink: /Java/StandardMBean/StandardMBean/
date: 2021-01-11
key: Java.S.StandardMBean
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardMBean.constructores valor="StandardMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected StandardMBean(Class<?> mbeanInterface) throws NotCompliantMBeanException
protected StandardMBean(Class<?> mbeanInterface, boolean isMXBean)
public StandardMBean(T implementation, Class<T> mbeanInterface) throws NotCompliantMBeanException
public StandardMBean(T implementation, Class<T> mbeanInterface, boolean isMXBean)
~~~

## Parámetros
* **boolean isMXBean**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isMXBean" %}
* **Class&lt;T&gt; mbeanInterface**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> mbeanInterface" %}
* **Class&lt;?&gt; mbeanInterface**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> mbeanInterface" %}
* **T implementation**,  {% include w3api/param_description.html metodo=_dato parametro="T implementation" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NotCompliantMBeanException](/Java/NotCompliantMBeanException/)

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
