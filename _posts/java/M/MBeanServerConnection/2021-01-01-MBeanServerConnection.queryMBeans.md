---
title: MBeanServerConnection.queryMBeans()
permalink: /Java/MBeanServerConnection/queryMBeans/
date: 2021-01-11
key: Java.M.MBeanServerConnection
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="queryMBeans" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Set<ObjectInstance> queryMBeans(ObjectName name, QueryExp query) throws IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **QueryExp query**,  {% include w3api/param_description.html metodo=_dato parametro="QueryExp query" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[MBeanServerConnection](/Java/MBeanServerConnection/)

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
