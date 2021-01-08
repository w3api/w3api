---
title: StandardMBean.StandardMBean()
permalink: Java/StandardMBean/StandardMBean
date: 2021-01-04
key: JavaJava.S.StandardMBean
category: java
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
* **boolean isMXBean**,  {% include w3api/param_description.html metodo=_data parametro="boolean isMXBean" %}
* **Class&lt;T&gt; mbeanInterface**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> mbeanInterface" %}
* **T implementation**,  {% include w3api/param_description.html metodo=_data parametro="T implementation" %}
* **Class&lt;?&gt; mbeanInterface**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> mbeanInterface" %}

## Excepciones
[NotCompliantMBeanException](/Java/NotCompliantMBeanException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
