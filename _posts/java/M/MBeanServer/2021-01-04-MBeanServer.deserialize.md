---
title: MBeanServer.deserialize()
permalink: Java/MBeanServer/deserialize
date: 2021-01-04
key: JavaJava.M.MBeanServer
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="deserialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="1.5") default ObjectInputStream deserialize(String className, byte[] data) throws OperationsException, ReflectionException
@Deprecated(since="1.5") default ObjectInputStream deserialize(String className, ObjectName loaderName, byte[] data) throws InstanceNotFoundException, OperationsException, ReflectionException
@Deprecated(since="1.5") default ObjectInputStream deserialize(ObjectName name, byte[] data) throws InstanceNotFoundException, OperationsException
~~~

## Parámetros
* **byte[] data**,  {% include w3api/param_description.html metodo=_data parametro="byte[] data" %}
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}
* **ObjectName loaderName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName loaderName" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [ReflectionException](/Java/ReflectionException/), [OperationsException](/Java/OperationsException/)

## Clase Padre
[MBeanServer](/Java/MBeanServer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
