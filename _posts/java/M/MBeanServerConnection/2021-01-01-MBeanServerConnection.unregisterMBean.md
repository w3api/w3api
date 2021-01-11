---
title: MBeanServerConnection.unregisterMBean()
permalink: Java/MBeanServerConnection/unregisterMBean
date: 2021-01-11
key: JavaJava.M.MBeanServerConnection
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="unregisterMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void unregisterMBean(ObjectName name) throws InstanceNotFoundException, MBeanRegistrationException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/), [MBeanRegistrationException](/Java/MBeanRegistrationException/), [RuntimeErrorException](/Java/RuntimeErrorException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeMBeanException](/Java/RuntimeMBeanException/)

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
