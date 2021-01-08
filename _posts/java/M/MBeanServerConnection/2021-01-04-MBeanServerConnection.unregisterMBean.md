---
title: MBeanServerConnection.unregisterMBean()
permalink: Java/MBeanServerConnection/unregisterMBean
date: 2021-01-04
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
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}

## Excepciones
[RuntimeErrorException](/Java/RuntimeErrorException/), [MBeanRegistrationException](/Java/MBeanRegistrationException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeMBeanException](/Java/RuntimeMBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/)

## Clase Padre
[MBeanServerConnection](/Java/MBeanServerConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
