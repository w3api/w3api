---
title: RMIConnection.createMBean()
permalink: Java/RMIConnection/createMBean
date: 2021-01-04
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="createMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectInstance createMBean(String className, ObjectName name, MarshalledObject params, String[] signature, Subject delegationSubject) throws ReflectionException, InstanceAlreadyExistsException, MBeanRegistrationException, MBeanException, NotCompliantMBeanException, IOException
ObjectInstance createMBean(String className, ObjectName name, ObjectName loaderName, MarshalledObject params, String[] signature, Subject delegationSubject) throws ReflectionException, InstanceAlreadyExistsException, MBeanRegistrationException, MBeanException, NotCompliantMBeanException, InstanceNotFoundException, IOException
ObjectInstance createMBean(String className, ObjectName name, ObjectName loaderName, Subject delegationSubject) throws ReflectionException, InstanceAlreadyExistsException, MBeanRegistrationException, MBeanException, NotCompliantMBeanException, InstanceNotFoundException, IOException
ObjectInstance createMBean(String className, ObjectName name, Subject delegationSubject) throws ReflectionException, InstanceAlreadyExistsException, MBeanRegistrationException, MBeanException, NotCompliantMBeanException, IOException
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_data parametro="Subject delegationSubject" %}
* **ObjectName loaderName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName loaderName" %}
* **String[] signature**,  {% include w3api/param_description.html metodo=_data parametro="String[] signature" %}
* **MarshalledObject params**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject params" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NotCompliantMBeanException](/Java/NotCompliantMBeanException/), [MBeanRegistrationException](/Java/MBeanRegistrationException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [ReflectionException](/Java/ReflectionException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [InstanceAlreadyExistsException](/Java/InstanceAlreadyExistsException/), [IOException](/Java/IOException/)

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
