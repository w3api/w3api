---
title: StandardMBean.getConstructors()
permalink: Java/StandardMBean/getConstructors
date: 2021-01-11
key: JavaJava.S.StandardMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardMBean.metodos valor="getConstructors" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected MBeanConstructorInfo[] getConstructors(MBeanConstructorInfo[] ctors, Object impl)
~~~

## Parámetros
* **Object impl**,  {% include w3api/param_description.html metodo=_dato parametro="Object impl" %}
* **MBeanConstructorInfo[] ctors**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanConstructorInfo[] ctors" %}

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
