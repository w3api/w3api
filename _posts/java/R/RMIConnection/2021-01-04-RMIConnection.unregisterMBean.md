---
title: RMIConnection.unregisterMBean()
permalink: Java/RMIConnection/unregisterMBean
date: 2021-01-04
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="unregisterMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void unregisterMBean(ObjectName name, Subject delegationSubject) throws InstanceNotFoundException, MBeanRegistrationException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_data parametro="Subject delegationSubject" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [MBeanRegistrationException](/Java/MBeanRegistrationException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
